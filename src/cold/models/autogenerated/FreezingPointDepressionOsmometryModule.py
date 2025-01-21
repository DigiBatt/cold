
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .OsmometryModule import Osmometry







class FreezingPointDepressionOsmometry(Osmometry):
    """
    Class representing the `FreezingPointDepressionOsmometry` entity, which inherits from:
    - Osmometry

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/characterisation-methodology/chameo#FreezingPointDepressionOsmometry'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'FreezingPointDepressionOsmometry'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = FreezingPointDepressionOsmometry(
    
    class_iri='https://w3id.org/emmo/domain/characterisation-methodology/chameo#FreezingPointDepressionOsmometry',
    
    class_name='FreezingPointDepressionOsmometry',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/characterisation-methodology/chameo#FreezingPointDepressionOsmometry',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'FreezingPointDepressionOsmometry',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    