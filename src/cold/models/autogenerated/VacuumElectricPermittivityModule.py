
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .PermittivityModule import Permittivity



from .MeasuredConstantModule import MeasuredConstant







class VacuumElectricPermittivity(Permittivity, MeasuredConstant):
    """
    Class representing the `VacuumElectricPermittivity` entity, which inherits from:
    - Permittivity, MeasuredConstant

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_61a32ae9_8200_473a_bd55_59a9899996f4'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'VacuumElectricPermittivity'`
        - **Alias**: `class_name`
    
    - `iupacReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `iupacReference`
    
    - `qudtReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `qudtReference`
    
    - `ISO80000Reference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `ISO80000Reference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = VacuumElectricPermittivity(
    
    class_iri='https://w3id.org/emmo#EMMO_61a32ae9_8200_473a_bd55_59a9899996f4',
    
    class_name='VacuumElectricPermittivity',
    
    iupacReference="example_value",
    
    qudtReference="example_value",
    
    ISO80000Reference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_61a32ae9_8200_473a_bd55_59a9899996f4',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'VacuumElectricPermittivity',
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
    
    ISO80000Reference: Optional[str] = Field(
        None,
        alias="ISO80000Reference"
    )
    

    
    

    

    