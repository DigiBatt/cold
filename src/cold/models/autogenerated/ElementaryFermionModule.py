
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .FermionModule import Fermion



from .ElementaryParticleModule import ElementaryParticle







class ElementaryFermion(Fermion, ElementaryParticle):
    """
    Class representing the `ElementaryFermion` entity, which inherits from:
    - Fermion, ElementaryParticle

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_820619ca_b23e_4c7a_8543_18a17722abc0'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ElementaryFermion'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ElementaryFermion(
    
    class_iri='https://w3id.org/emmo#EMMO_820619ca_b23e_4c7a_8543_18a17722abc0',
    
    class_name='ElementaryFermion',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_820619ca_b23e_4c7a_8543_18a17722abc0',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ElementaryFermion',
        alias="class_name"
    )
    

    
    

    

    