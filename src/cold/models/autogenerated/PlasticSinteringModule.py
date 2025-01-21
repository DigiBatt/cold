
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SinteringModule import Sintering







class PlasticSintering(Sintering):
    """
    Class representing the `PlasticSintering` entity, which inherits from:
    - Sintering

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_08d993e0_cc1c_45da_b0c5_3d658091ccfd'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'PlasticSintering'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = PlasticSintering(
    
    class_iri='https://w3id.org/emmo#EMMO_08d993e0_cc1c_45da_b0c5_3d658091ccfd',
    
    class_name='PlasticSintering',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_08d993e0_cc1c_45da_b0c5_3d658091ccfd',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'PlasticSintering',
        alias="class_name"
    )
    

    
    

    

    