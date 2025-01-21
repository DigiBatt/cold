
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .IntentionalProcessModule import IntentionalProcess







class IntentionalBatteryProcess(IntentionalProcess):
    """
    Class representing the `IntentionalBatteryProcess` entity, which inherits from:
    - IntentionalProcess

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/battery#battery_7c072505_7ea6_4bfd_8403_7133b3a4b806'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'IntentionalBatteryProcess'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = IntentionalBatteryProcess(
    
    class_iri='https://w3id.org/emmo/domain/battery#battery_7c072505_7ea6_4bfd_8403_7133b3a4b806',
    
    class_name='IntentionalBatteryProcess',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/battery#battery_7c072505_7ea6_4bfd_8403_7133b3a4b806',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'IntentionalBatteryProcess',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    