
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MeasuredConstantModule import MeasuredConstant



from .WavenumberModule import Wavenumber







class RybergConstant(MeasuredConstant, Wavenumber):
    """
    Class representing the `RybergConstant` entity, which inherits from:
    - MeasuredConstant, Wavenumber

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_a3c78d6f_ae49_47c8_a634_9b6d86b79382'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'RybergConstant'`
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
    obj = RybergConstant(
    
    class_iri='https://w3id.org/emmo#EMMO_a3c78d6f_ae49_47c8_a634_9b6d86b79382',
    
    class_name='RybergConstant',
    
    iupacReference="example_value",
    
    qudtReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_a3c78d6f_ae49_47c8_a634_9b6d86b79382',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'RybergConstant',
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
    

    
    

    

    