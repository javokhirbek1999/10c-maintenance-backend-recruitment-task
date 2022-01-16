from django.db import models


class Investor(models.Model):
    name = models.CharField(
        max_length=255, help_text="Investor name"
    )
    remaining_amount = models.DecimalField(
        max_digits=11, decimal_places=2, help_text="Remaining investor's amount.", default=0
    )
    total_amount = models.DecimalField(
        max_digits=11, decimal_places=2, help_text="Total investor's amount."
    )
    individual_amount = models.DecimalField(
        max_digits=11,
        decimal_places=2,
        help_text="Individual amount per project",
    )
    project_delivery_deadline = models.DateField(
        help_text="Deadline that funded projects must deliver by"
    )


    def matching_projects(self):

        """
        Function to filter all matching projects for given investor by following criteria:

        - Project is not already funded
        - Investor's per project funding is greater or equal to amount needed by Project
        - Investor has enough funds to invest into Project
        - Projects that can be delivered within Investor's deadline

        """

        projects = Project.objects.filter(
            funded=False,
            amount__lte=self.individual_amount,
            delivery_date__lte=self.project_delivery_deadline).filter(amount__lte=self.remaining_amount)

        return projects
    
    @property
    def matching_project_ids(self):
        
        """
            Returns list of matching project IDs
        """
        if len(self.matching_projects())==0:
            return []
        return [project.id for project in self.matching_projects()]


    def __str__(self):
        return f"Investor: {self.name}"


class Project(models.Model):
    name = models.CharField(
        "Project's name",
        max_length=255,
        help_text="Name of the project",
    )
    description = models.TextField(
        max_length=700,
        help_text="What’s the goal of the project?"
    )
    amount = models.DecimalField(
        help_text="Total project funding required",
        decimal_places=2,
        max_digits=7,
    )
    delivery_date = models.DateField(
        help_text="Estimated project delivery date."
    )
    funded_by = models.ForeignKey(Investor, null=True, blank=True, editable=False,
                                  related_name="funded_projects", on_delete=models.SET_NULL)
    # This is a backup field in case investor gets deleted and funded_by is NULL
    funded = models.BooleanField(default=False, editable=False)


    def matching_investors(self):
        """
            Function to filter all matching investors for given project by following criteria:

            - Investors that have enough funds to invest into Project
            - Investors' per project funding is greater or equal to amount needed by Project
            - Projects that can be delivered within Investor's deadline
        """

        investors = Investor.objects.filter(
        remaining_amount__gte=self.amount,
        individual_amount__gte=self.amount,
        project_delivery_deadline__gte=self.delivery_date)
    
        return investors
    
    @property
    def matching_investor_ids(self):
        """
            Returns list of matching investor IDs
        """

        if len(self.matching_investors())==0:
            return []
        return [investor.id for investor in self.matching_investors()]

    def __str__(self):
        return f"Project: {self.name}"
