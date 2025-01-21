
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .DeviceModule import Device







class ManufacturingDevice(Device):
    """
    Class representing the `ManufacturingDevice` entity, which inherits from:
    - Device

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_86a305d1_7644_48be_b84c_1f976679b904'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ManufacturingDevice'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ManufacturingDevice(
    
    class_iri='https://w3id.org/emmo#EMMO_86a305d1_7644_48be_b84c_1f976679b904',
    
    class_name='ManufacturingDevice',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_86a305d1_7644_48be_b84c_1f976679b904',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ManufacturingDevice',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    