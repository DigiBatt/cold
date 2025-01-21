
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectrochemicalInterfaceModule import ElectrochemicalInterface







class BatteryInterface(ElectrochemicalInterface):
    """
    Class representing the `BatteryInterface` entity, which inherits from:
    - ElectrochemicalInterface

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/battery#battery_5129704d_3e08_4bee_b2d3_7b9e193cb481'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'BatteryInterface'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = BatteryInterface(
    
    class_iri='https://w3id.org/emmo/domain/battery#battery_5129704d_3e08_4bee_b2d3_7b9e193cb481',
    
    class_name='BatteryInterface',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/battery#battery_5129704d_3e08_4bee_b2d3_7b9e193cb481',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'BatteryInterface',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    