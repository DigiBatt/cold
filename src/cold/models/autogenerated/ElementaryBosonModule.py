
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElementaryParticleModule import ElementaryParticle



from .BosonModule import Boson







class ElementaryBoson(ElementaryParticle, Boson):
    """
    Class representing the `ElementaryBoson` entity, which inherits from:
    - ElementaryParticle, Boson

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_cafd0f10_ce85_48b9_9a36_2b0af141ce21'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ElementaryBoson'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ElementaryBoson(
    
    class_iri='https://w3id.org/emmo#EMMO_cafd0f10_ce85_48b9_9a36_2b0af141ce21',
    
    class_name='ElementaryBoson',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_cafd0f10_ce85_48b9_9a36_2b0af141ce21',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ElementaryBoson',
        alias="class_name"
    )
    

    
    

    

    