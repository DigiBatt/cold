
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MixtureModule import Mixture







class Dispersion(Mixture):
    """
    Class representing the `Dispersion` entity, which inherits from:
    - Mixture

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_0b15f4ae_092e_4487_9100_3c44176c545c'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Dispersion'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Dispersion(
    
    class_iri='https://w3id.org/emmo#EMMO_0b15f4ae_092e_4487_9100_3c44176c545c',
    
    class_name='Dispersion',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_0b15f4ae_092e_4487_9100_3c44176c545c',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Dispersion',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    