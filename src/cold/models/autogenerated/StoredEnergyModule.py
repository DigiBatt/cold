
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .EnergyModule import Energy



from .ElectrochemicalPerformanceQuantityModule import ElectrochemicalPerformanceQuantity







class StoredEnergy(Energy, ElectrochemicalPerformanceQuantity):
    """
    Class representing the `StoredEnergy` entity, which inherits from:
    - Energy, ElectrochemicalPerformanceQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_46376e5d_9627_4514_9881_9e62083625c3'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'StoredEnergy'`
        - **Alias**: `class_name`
    
    - `maccorLabel` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `maccorLabel`
    
    - `indigoLabel` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `indigoLabel`
    
    - `novonixLabel` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `novonixLabel`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `newareLabel` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `newareLabel`
    
    - `IEVReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `IEVReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = StoredEnergy(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_46376e5d_9627_4514_9881_9e62083625c3',
    
    class_name='StoredEnergy',
    
    maccorLabel="example_value",
    
    indigoLabel="example_value",
    
    novonixLabel="example_value",
    
    elucidation="example_value",
    
    newareLabel="example_value",
    
    IEVReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_46376e5d_9627_4514_9881_9e62083625c3',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'StoredEnergy',
        alias="class_name"
    )
    
    maccorLabel: Optional[str] = Field(
        None,
        alias="maccorLabel"
    )
    
    indigoLabel: Optional[str] = Field(
        None,
        alias="indigoLabel"
    )
    
    novonixLabel: Optional[str] = Field(
        None,
        alias="novonixLabel"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    newareLabel: Optional[str] = Field(
        None,
        alias="newareLabel"
    )
    
    IEVReference: Optional[str] = Field(
        None,
        alias="IEVReference"
    )
    

    
    

    

    