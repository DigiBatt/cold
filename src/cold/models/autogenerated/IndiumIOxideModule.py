
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .IndiumOxideCompoundModule import IndiumOxideCompound







class IndiumIOxide(IndiumOxideCompound):
    """
    Class representing the `IndiumIOxide` entity, which inherits from:
    - IndiumOxideCompound

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_8018d7e8_c3f3_411e_adda_644bbd53338d'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'IndiumIOxide'`
        - **Alias**: `class_name`
    
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
    obj = IndiumIOxide(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_8018d7e8_c3f3_411e_adda_644bbd53338d',
    
    class_name='IndiumIOxide',
    
    pubChemReference="example_value",
    
    wikidataReference="example_value",
    
    standardInChI="example_value",
    
    molecularFormula="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_8018d7e8_c3f3_411e_adda_644bbd53338d',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'IndiumIOxide',
        alias="class_name"
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
    

    
    

    

    