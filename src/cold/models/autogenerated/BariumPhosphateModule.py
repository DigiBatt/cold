
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .BariumSaltCompoundModule import BariumSaltCompound







class BariumPhosphate(BariumSaltCompound):
    """
    Class representing the `BariumPhosphate` entity, which inherits from:
    - BariumSaltCompound

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_8cbdf192_69bf_45cc_a570_95bf69fd8f91'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'BariumPhosphate'`
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
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = BariumPhosphate(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_8cbdf192_69bf_45cc_a570_95bf69fd8f91',
    
    class_name='BariumPhosphate',
    
    IUPACName="example_value",
    
    pubChemReference="example_value",
    
    wikidataReference="example_value",
    
    standardInChI="example_value",
    
    molecularFormula="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_8cbdf192_69bf_45cc_a570_95bf69fd8f91',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'BariumPhosphate',
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
    

    
    

    

    