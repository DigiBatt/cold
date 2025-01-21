
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MeasuredConstantModule import MeasuredConstant



from .MassModule import Mass







class ProtonMass(MeasuredConstant, Mass):
    """
    Class representing the `ProtonMass` entity, which inherits from:
    - MeasuredConstant, Mass

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_8d689295_7d84_421b_bc01_d5cceb2c2086'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ProtonMass'`
        - **Alias**: `class_name`
    
    - `iupacReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `iupacReference`
    
    - `qudtReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `qudtReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ProtonMass(
    
    class_iri='https://w3id.org/emmo#EMMO_8d689295_7d84_421b_bc01_d5cceb2c2086',
    
    class_name='ProtonMass',
    
    iupacReference="example_value",
    
    qudtReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_8d689295_7d84_421b_bc01_d5cceb2c2086',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ProtonMass',
        alias="class_name"
    )
    
    iupacReference: Optional[str] = Field(
        None,
        alias="iupacReference"
    )
    
    qudtReference: Optional[str] = Field(
        None,
        alias="qudtReference"
    )
    

    
    

    

    