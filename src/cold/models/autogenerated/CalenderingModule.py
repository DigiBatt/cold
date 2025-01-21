
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .FormingFromPlasticModule import FormingFromPlastic







class Calendering(FormingFromPlastic):
    """
    Class representing the `Calendering` entity, which inherits from:
    - FormingFromPlastic

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_c7f4684e_ee74_4119_87e0_ecd255e10d2f'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Calendering'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Calendering(
    
    class_iri='https://w3id.org/emmo#EMMO_c7f4684e_ee74_4119_87e0_ecd255e10d2f',
    
    class_name='Calendering',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_c7f4684e_ee74_4119_87e0_ecd255e10d2f',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Calendering',
        alias="class_name"
    )
    

    
    

    

    