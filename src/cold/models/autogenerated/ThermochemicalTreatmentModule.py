
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .HeatTreatmentModule import HeatTreatment







class ThermochemicalTreatment(HeatTreatment):
    """
    Class representing the `ThermochemicalTreatment` entity, which inherits from:
    - HeatTreatment

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_263d9161_5a7c_4900_a49b_55f012b3fe07'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ThermochemicalTreatment'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ThermochemicalTreatment(
    
    class_iri='https://w3id.org/emmo#EMMO_263d9161_5a7c_4900_a49b_55f012b3fe07',
    
    class_name='ThermochemicalTreatment',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_263d9161_5a7c_4900_a49b_55f012b3fe07',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ThermochemicalTreatment',
        alias="class_name"
    )
    

    
    

    

    