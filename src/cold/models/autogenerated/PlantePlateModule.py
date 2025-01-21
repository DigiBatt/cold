
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CoatedElectrodeModule import CoatedElectrode







class PlantePlate(CoatedElectrode):
    """
    Class representing the `PlantePlate` entity, which inherits from:
    - CoatedElectrode

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/battery#battery_9d625cce_b579_4a6b_9e92_079f2c5a29bb'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'PlantePlate'`
        - **Alias**: `class_name`
    
    - `IEVReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `IEVReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = PlantePlate(
    
    class_iri='https://w3id.org/emmo/domain/battery#battery_9d625cce_b579_4a6b_9e92_079f2c5a29bb',
    
    class_name='PlantePlate',
    
    IEVReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/battery#battery_9d625cce_b579_4a6b_9e92_079f2c5a29bb',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'PlantePlate',
        alias="class_name"
    )
    
    IEVReference: Optional[str] = Field(
        None,
        alias="IEVReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    