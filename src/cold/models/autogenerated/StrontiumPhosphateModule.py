
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .StrontiumSaltCompoundModule import StrontiumSaltCompound







class StrontiumPhosphate(StrontiumSaltCompound):
    """
    Class representing the `StrontiumPhosphate` entity, which inherits from:
    - StrontiumSaltCompound

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_e128782f_8c69_43b2_9c3c_9efb31e8a6b5'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'StrontiumPhosphate'`
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
    obj = StrontiumPhosphate(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_e128782f_8c69_43b2_9c3c_9efb31e8a6b5',
    
    class_name='StrontiumPhosphate',
    
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
        'https://w3id.org/emmo/domain/chemical-substance#substance_e128782f_8c69_43b2_9c3c_9efb31e8a6b5',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'StrontiumPhosphate',
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
    

    
    

    

    