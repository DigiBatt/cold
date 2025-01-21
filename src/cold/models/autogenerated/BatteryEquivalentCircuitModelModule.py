
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectrochemicalEquivalentCircuitModelModule import ElectrochemicalEquivalentCircuitModel







class BatteryEquivalentCircuitModel(ElectrochemicalEquivalentCircuitModel):
    """
    Class representing the `BatteryEquivalentCircuitModel` entity, which inherits from:
    - ElectrochemicalEquivalentCircuitModel

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/battery#battery_4c78a492_b14d_4005_b555_d3c92e8def0f'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'BatteryEquivalentCircuitModel'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = BatteryEquivalentCircuitModel(
    
    class_iri='https://w3id.org/emmo/domain/battery#battery_4c78a492_b14d_4005_b555_d3c92e8def0f',
    
    class_name='BatteryEquivalentCircuitModel',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/battery#battery_4c78a492_b14d_4005_b555_d3c92e8def0f',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'BatteryEquivalentCircuitModel',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    