
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .FormingFromPlasticModule import FormingFromPlastic







class DrawForms(FormingFromPlastic):
    """
    Class representing the `DrawForms` entity, which inherits from:
    - FormingFromPlastic

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_d02f6f3e_9e32_4188_a116_29dc304ceb49'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'DrawForms'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = DrawForms(
    
    class_iri='https://w3id.org/emmo#EMMO_d02f6f3e_9e32_4188_a116_29dc304ceb49',
    
    class_name='DrawForms',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_d02f6f3e_9e32_4188_a116_29dc304ceb49',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'DrawForms',
        alias="class_name"
    )
    

    
    

    

    