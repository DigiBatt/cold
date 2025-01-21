
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SpecificHeatCapacityModule import SpecificHeatCapacity







class DeviceLumpedSpecificHeatCapacity(SpecificHeatCapacity):
    """
    Class representing the `DeviceLumpedSpecificHeatCapacity` entity, which inherits from:
    - SpecificHeatCapacity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_9cba2158_26ba_4dd7_b082_ba66dbb960c7'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'DeviceLumpedSpecificHeatCapacity'`
        - **Alias**: `class_name`
    
    - `cidemodKey` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `cidemodKey`
    
    - `bpxKey` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `bpxKey`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = DeviceLumpedSpecificHeatCapacity(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_9cba2158_26ba_4dd7_b082_ba66dbb960c7',
    
    class_name='DeviceLumpedSpecificHeatCapacity',
    
    cidemodKey="example_value",
    
    bpxKey="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_9cba2158_26ba_4dd7_b082_ba66dbb960c7',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'DeviceLumpedSpecificHeatCapacity',
        alias="class_name"
    )
    
    cidemodKey: Optional[str] = Field(
        None,
        alias="cidemodKey"
    )
    
    bpxKey: Optional[str] = Field(
        None,
        alias="bpxKey"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    