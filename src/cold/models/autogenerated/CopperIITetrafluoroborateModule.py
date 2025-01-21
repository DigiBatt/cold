
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CopperSaltCompoundModule import CopperSaltCompound







class CopperIITetrafluoroborate(CopperSaltCompound):
    """
    Class representing the `CopperIITetrafluoroborate` entity, which inherits from:
    - CopperSaltCompound

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_dfa3d84e_279c_47d0_ad87_5a30b1a325ce'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CopperIITetrafluoroborate'`
        - **Alias**: `class_name`
    
    - `IUPACName` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `IUPACName`
    
    - `pubChemReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `pubChemReference`
    
    - `standardInChI` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `standardInChI`
    
    - `molecularFormula` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `molecularFormula`
    
    - `wikipediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikipediaReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = CopperIITetrafluoroborate(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_dfa3d84e_279c_47d0_ad87_5a30b1a325ce',
    
    class_name='CopperIITetrafluoroborate',
    
    IUPACName="example_value",
    
    pubChemReference="example_value",
    
    standardInChI="example_value",
    
    molecularFormula="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_dfa3d84e_279c_47d0_ad87_5a30b1a325ce',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'CopperIITetrafluoroborate',
        alias="class_name"
    )
    
    IUPACName: Optional[str] = Field(
        None,
        alias="IUPACName"
    )
    
    pubChemReference: Optional[str] = Field(
        None,
        alias="pubChemReference"
    )
    
    standardInChI: Optional[str] = Field(
        None,
        alias="standardInChI"
    )
    
    molecularFormula: Optional[str] = Field(
        None,
        alias="molecularFormula"
    )
    
    wikipediaReference: Optional[str] = Field(
        None,
        alias="wikipediaReference"
    )
    

    
    

    

    