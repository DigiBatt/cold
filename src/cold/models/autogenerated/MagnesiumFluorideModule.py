
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MagnesiumSaltCompoundModule import MagnesiumSaltCompound







class MagnesiumFluoride(MagnesiumSaltCompound):
    """
    Class representing the `MagnesiumFluoride` entity, which inherits from:
    - MagnesiumSaltCompound

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_5263c4d3_8759_48a1_b35e_5abf7a1f0454'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MagnesiumFluoride'`
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
    obj = MagnesiumFluoride(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_5263c4d3_8759_48a1_b35e_5abf7a1f0454',
    
    class_name='MagnesiumFluoride',
    
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
        'https://w3id.org/emmo/domain/chemical-substance#substance_5263c4d3_8759_48a1_b35e_5abf7a1f0454',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'MagnesiumFluoride',
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
    

    
    

    

    