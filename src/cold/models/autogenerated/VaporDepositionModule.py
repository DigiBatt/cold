
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .FormingFromGasModule import FormingFromGas







class VaporDeposition(FormingFromGas):
    """
    Class representing the `VaporDeposition` entity, which inherits from:
    - FormingFromGas

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_68d094e2_1777_48b5_8e43_32965f824970'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'VaporDeposition'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = VaporDeposition(
    
    class_iri='https://w3id.org/emmo#EMMO_68d094e2_1777_48b5_8e43_32965f824970',
    
    class_name='VaporDeposition',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_68d094e2_1777_48b5_8e43_32965f824970',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'VaporDeposition',
        alias="class_name"
    )
    

    
    

    

    