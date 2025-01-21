
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .NickelSaltCompoundModule import NickelSaltCompound







class NickelIIHexafluorophosphate(NickelSaltCompound):
    """
    Class representing the `NickelIIHexafluorophosphate` entity, which inherits from:
    - NickelSaltCompound

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_4ed2fb2e_2e73_43c1_bc98_4d0ee34f859e'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'NickelIIHexafluorophosphate'`
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
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = NickelIIHexafluorophosphate(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_4ed2fb2e_2e73_43c1_bc98_4d0ee34f859e',
    
    class_name='NickelIIHexafluorophosphate',
    
    IUPACName="example_value",
    
    pubChemReference="example_value",
    
    standardInChI="example_value",
    
    molecularFormula="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_4ed2fb2e_2e73_43c1_bc98_4d0ee34f859e',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'NickelIIHexafluorophosphate',
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
    

    
    

    

    