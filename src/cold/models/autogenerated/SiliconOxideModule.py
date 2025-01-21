
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .NonMetalOxideModule import NonMetalOxide







class SiliconOxide(NonMetalOxide):
    """
    Class representing the `SiliconOxide` entity, which inherits from:
    - NonMetalOxide

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_0160f86c_e567_40d4_a457_25cf170e7ef2'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SiliconOxide'`
        - **Alias**: `class_name`
    
    - `wikidataReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikidataReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `molecularFormula` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `molecularFormula`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = SiliconOxide(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_0160f86c_e567_40d4_a457_25cf170e7ef2',
    
    class_name='SiliconOxide',
    
    wikidataReference="example_value",
    
    elucidation="example_value",
    
    molecularFormula="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_0160f86c_e567_40d4_a457_25cf170e7ef2',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SiliconOxide',
        alias="class_name"
    )
    
    wikidataReference: Optional[str] = Field(
        None,
        alias="wikidataReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    molecularFormula: Optional[str] = Field(
        None,
        alias="molecularFormula"
    )
    

    
    

    

    