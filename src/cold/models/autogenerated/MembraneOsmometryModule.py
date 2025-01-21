
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .OsmometryModule import Osmometry







class MembraneOsmometry(Osmometry):
    """
    Class representing the `MembraneOsmometry` entity, which inherits from:
    - Osmometry

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/characterisation-methodology/chameo#MembraneOsmometry'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MembraneOsmometry'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = MembraneOsmometry(
    
    class_iri='https://w3id.org/emmo/domain/characterisation-methodology/chameo#MembraneOsmometry',
    
    class_name='MembraneOsmometry',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/characterisation-methodology/chameo#MembraneOsmometry',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'MembraneOsmometry',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    