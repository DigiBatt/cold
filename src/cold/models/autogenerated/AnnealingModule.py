
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .HeatTreatmentModule import HeatTreatment







class Annealing(HeatTreatment):
    """
    Class representing the `Annealing` entity, which inherits from:
    - HeatTreatment

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_9900d51c_bdd3_40e8_aa82_ad1aa7092f71'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Annealing'`
        - **Alias**: `class_name`
    
    - `comment` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `comment`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Annealing(
    
    class_iri='https://w3id.org/emmo#EMMO_9900d51c_bdd3_40e8_aa82_ad1aa7092f71',
    
    class_name='Annealing',
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_9900d51c_bdd3_40e8_aa82_ad1aa7092f71',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Annealing',
        alias="class_name"
    )
    
    comment: Optional[str] = Field(
        None,
        alias="comment"
    )
    

    
    

    

    