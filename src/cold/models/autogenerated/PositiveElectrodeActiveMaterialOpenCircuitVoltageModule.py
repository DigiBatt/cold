
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SourceVoltageModule import SourceVoltage



from .OpenCircuitVoltageModule import OpenCircuitVoltage







class PositiveElectrodeActiveMaterialOpenCircuitVoltage(SourceVoltage, OpenCircuitVoltage):
    """
    Class representing the `PositiveElectrodeActiveMaterialOpenCircuitVoltage` entity, which inherits from:
    - SourceVoltage, OpenCircuitVoltage

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_52ab4fdd_f945_4541_9ce6_cd6fd3a05861'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'PositiveElectrodeActiveMaterialOpenCircuitVoltage'`
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
    obj = PositiveElectrodeActiveMaterialOpenCircuitVoltage(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_52ab4fdd_f945_4541_9ce6_cd6fd3a05861',
    
    class_name='PositiveElectrodeActiveMaterialOpenCircuitVoltage',
    
    cidemodKey="example_value",
    
    bpxKey="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_52ab4fdd_f945_4541_9ce6_cd6fd3a05861',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'PositiveElectrodeActiveMaterialOpenCircuitVoltage',
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
    

    
    

    

    