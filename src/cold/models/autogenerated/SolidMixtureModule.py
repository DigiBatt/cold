
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SolidModule import Solid



from .MixtureModule import Mixture







class SolidMixture(Solid, Mixture):
    """
    Class representing the `SolidMixture` entity, which inherits from:
    - Solid, Mixture

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_77e2e601_5ecb_450b_b563_92f096997832'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SolidMixture'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = SolidMixture(
    
    class_iri='https://w3id.org/emmo#EMMO_77e2e601_5ecb_450b_b563_92f096997832',
    
    class_name='SolidMixture',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_77e2e601_5ecb_450b_b563_92f096997832',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SolidMixture',
        alias="class_name"
    )
    

    
    

    

    