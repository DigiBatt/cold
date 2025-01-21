
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .AlkalineZincManganeseDioxideBatteryModule import AlkalineZincManganeseDioxideBattery







class AlkalineLanternBattery(AlkalineZincManganeseDioxideBattery):
    """
    Class representing the `AlkalineLanternBattery` entity, which inherits from:
    - AlkalineZincManganeseDioxideBattery

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/battery#battery_cbc032aa_657f_4dca_87f8_edaccc70348d'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'AlkalineLanternBattery'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = AlkalineLanternBattery(
    
    class_iri='https://w3id.org/emmo/domain/battery#battery_cbc032aa_657f_4dca_87f8_edaccc70348d',
    
    class_name='AlkalineLanternBattery',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/battery#battery_cbc032aa_657f_4dca_87f8_edaccc70348d',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'AlkalineLanternBattery',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    