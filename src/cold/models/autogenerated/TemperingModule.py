
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .HeatTreatmentModule import HeatTreatment







class Tempering(HeatTreatment):
    """
    Class representing the `Tempering` entity, which inherits from:
    - HeatTreatment

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_6fa330f7_3289_4228_81df_12ee8a9708ac'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Tempering'`
        - **Alias**: `class_name`
    
    - `comment` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `comment`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Tempering(
    
    class_iri='https://w3id.org/emmo#EMMO_6fa330f7_3289_4228_81df_12ee8a9708ac',
    
    class_name='Tempering',
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_6fa330f7_3289_4228_81df_12ee8a9708ac',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Tempering',
        alias="class_name"
    )
    
    comment: Optional[str] = Field(
        None,
        alias="comment"
    )
    

    
    

    

    