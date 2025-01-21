
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .PhysicalPhenomenonModule import PhysicalPhenomenon







class BatteryPhenomenon(PhysicalPhenomenon):
    """
    Class representing the `BatteryPhenomenon` entity, which inherits from:
    - PhysicalPhenomenon

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/battery#battery_f768ea27_09ba_4875_a5cc_2c644b0753a3'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'BatteryPhenomenon'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = BatteryPhenomenon(
    
    class_iri='https://w3id.org/emmo/domain/battery#battery_f768ea27_09ba_4875_a5cc_2c644b0753a3',
    
    class_name='BatteryPhenomenon',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/battery#battery_f768ea27_09ba_4875_a5cc_2c644b0753a3',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'BatteryPhenomenon',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    