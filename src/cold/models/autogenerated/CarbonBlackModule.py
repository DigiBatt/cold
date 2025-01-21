
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CarbonElementalSubstanceModule import CarbonElementalSubstance







class CarbonBlack(CarbonElementalSubstance):
    """
    Class representing the `CarbonBlack` entity, which inherits from:
    - CarbonElementalSubstance

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_0a5cb747_60cf_4929_a54a_712c54b49f3b'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CarbonBlack'`
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
    obj = CarbonBlack(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_0a5cb747_60cf_4929_a54a_712c54b49f3b',
    
    class_name='CarbonBlack',
    
    wikidataReference="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_0a5cb747_60cf_4929_a54a_712c54b49f3b',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'CarbonBlack',
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
    

    
    

    

    