
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .VandaiumOxideCompoundModule import VandaiumOxideCompound







class VanadiumIIIOxide(VandaiumOxideCompound):
    """
    Class representing the `VanadiumIIIOxide` entity, which inherits from:
    - VandaiumOxideCompound

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_4796594d_8de9_482d_9644_7ee776941dc2'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'VanadiumIIIOxide'`
        - **Alias**: `class_name`
    
    - `IUPACName` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `IUPACName`
    
    - `pubChemReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `pubChemReference`
    
    - `wikidataReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikidataReference`
    
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
    obj = VanadiumIIIOxide(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_4796594d_8de9_482d_9644_7ee776941dc2',
    
    class_name='VanadiumIIIOxide',
    
    IUPACName="example_value",
    
    pubChemReference="example_value",
    
    wikidataReference="example_value",
    
    standardInChI="example_value",
    
    molecularFormula="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_4796594d_8de9_482d_9644_7ee776941dc2',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'VanadiumIIIOxide',
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
    
    wikidataReference: Optional[str] = Field(
        None,
        alias="wikidataReference"
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
    

    
    

    

    