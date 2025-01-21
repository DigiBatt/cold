
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CoatedElectrodeModule import CoatedElectrode







class PocketPlate(CoatedElectrode):
    """
    Class representing the `PocketPlate` entity, which inherits from:
    - CoatedElectrode

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/battery#battery_557c1a8f_0e10_423c_9ab8_5bc316056ef4'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'PocketPlate'`
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
    obj = PocketPlate(
    
    class_iri='https://w3id.org/emmo/domain/battery#battery_557c1a8f_0e10_423c_9ab8_5bc316056ef4',
    
    class_name='PocketPlate',
    
    IEVReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/battery#battery_557c1a8f_0e10_423c_9ab8_5bc316056ef4',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'PocketPlate',
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
    

    
    

    

    