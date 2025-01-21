
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .OsmometryModule import Osmometry







class VaporPressureDepressionOsmometry(Osmometry):
    """
    Class representing the `VaporPressureDepressionOsmometry` entity, which inherits from:
    - Osmometry

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/characterisation-methodology/chameo#VaporPressureDepressionOsmometry'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'VaporPressureDepressionOsmometry'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = VaporPressureDepressionOsmometry(
    
    class_iri='https://w3id.org/emmo/domain/characterisation-methodology/chameo#VaporPressureDepressionOsmometry',
    
    class_name='VaporPressureDepressionOsmometry',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/characterisation-methodology/chameo#VaporPressureDepressionOsmometry',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'VaporPressureDepressionOsmometry',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    