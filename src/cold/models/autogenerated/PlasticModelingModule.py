
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .FormingFromPlasticModule import FormingFromPlastic







class PlasticModeling(FormingFromPlastic):
    """
    Class representing the `PlasticModeling` entity, which inherits from:
    - FormingFromPlastic

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_b5efbfa6_8610_4e3e_ad36_93e426bd873e'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'PlasticModeling'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = PlasticModeling(
    
    class_iri='https://w3id.org/emmo#EMMO_b5efbfa6_8610_4e3e_ad36_93e426bd873e',
    
    class_name='PlasticModeling',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_b5efbfa6_8610_4e3e_ad36_93e426bd873e',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'PlasticModeling',
        alias="class_name"
    )
    

    
    

    

    