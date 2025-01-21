
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .PhysicalConstantModule import PhysicalConstant







class MeasuredConstant(PhysicalConstant):
    """
    Class representing the `MeasuredConstant` entity, which inherits from:
    - PhysicalConstant

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_3f15d200_c97b_42c8_8ac0_d81d150361e2'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MeasuredConstant'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = MeasuredConstant(
    
    class_iri='https://w3id.org/emmo#EMMO_3f15d200_c97b_42c8_8ac0_d81d150361e2',
    
    class_name='MeasuredConstant',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_3f15d200_c97b_42c8_8ac0_d81d150361e2',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'MeasuredConstant',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    