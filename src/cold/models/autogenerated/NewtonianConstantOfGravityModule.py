
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MeasuredConstantModule import MeasuredConstant







class NewtonianConstantOfGravity(MeasuredConstant):
    """
    Class representing the `NewtonianConstantOfGravity` entity, which inherits from:
    - MeasuredConstant

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_da831168_975a_41f8_baae_279c298569da'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'NewtonianConstantOfGravity'`
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
    obj = NewtonianConstantOfGravity(
    
    class_iri='https://w3id.org/emmo#EMMO_da831168_975a_41f8_baae_279c298569da',
    
    class_name='NewtonianConstantOfGravity',
    
    iupacReference="example_value",
    
    qudtReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_da831168_975a_41f8_baae_279c298569da',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'NewtonianConstantOfGravity',
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
    

    
    

    

    