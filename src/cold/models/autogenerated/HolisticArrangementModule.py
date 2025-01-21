
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .HolisticSystemModule import HolisticSystem







class HolisticArrangement(HolisticSystem):
    """
    Class representing the `HolisticArrangement` entity, which inherits from:
    - HolisticSystem

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_b9522e56_1fac_4766_97e6_428605fabd3e'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'HolisticArrangement'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = HolisticArrangement(
    
    class_iri='https://w3id.org/emmo#EMMO_b9522e56_1fac_4766_97e6_428605fabd3e',
    
    class_name='HolisticArrangement',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_b9522e56_1fac_4766_97e6_428605fabd3e',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'HolisticArrangement',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    