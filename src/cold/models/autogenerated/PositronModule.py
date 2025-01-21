
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .AntiElectronTypeModule import AntiElectronType



from .FirstGenerationFermionModule import FirstGenerationFermion







class Positron(AntiElectronType, FirstGenerationFermion):
    """
    Class representing the `Positron` entity, which inherits from:
    - AntiElectronType, FirstGenerationFermion

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_26a38b26_38ea_4acf_b212_db9e34c71b7a'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Positron'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Positron(
    
    class_iri='https://w3id.org/emmo#EMMO_26a38b26_38ea_4acf_b212_db9e34c71b7a',
    
    class_name='Positron',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_26a38b26_38ea_4acf_b212_db9e34c71b7a',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Positron',
        alias="class_name"
    )
    

    
    

    

    