
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CarbonElementalSubstanceModule import CarbonElementalSubstance







class HardCarbon(CarbonElementalSubstance):
    """
    Class representing the `HardCarbon` entity, which inherits from:
    - CarbonElementalSubstance

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_5cee19d2_f916_4264_a8ed_efed13a808d2'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'HardCarbon'`
        - **Alias**: `class_name`
    
    - `wikidataReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikidataReference`
    
    - `wikipediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikipediaReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = HardCarbon(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_5cee19d2_f916_4264_a8ed_efed13a808d2',
    
    class_name='HardCarbon',
    
    wikidataReference="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_5cee19d2_f916_4264_a8ed_efed13a808d2',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'HardCarbon',
        alias="class_name"
    )
    
    wikidataReference: Optional[str] = Field(
        None,
        alias="wikidataReference"
    )
    
    wikipediaReference: Optional[str] = Field(
        None,
        alias="wikipediaReference"
    )
    

    
    

    

    