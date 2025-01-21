
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectricResistanceModule import ElectricResistance



from .ElectrochemicalPerformanceQuantityModule import ElectrochemicalPerformanceQuantity







class InternalResistance(ElectricResistance, ElectrochemicalPerformanceQuantity):
    """
    Class representing the `InternalResistance` entity, which inherits from:
    - ElectricResistance, ElectrochemicalPerformanceQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_9bf40017_3f58_4030_ada7_cb37a3dfda2d'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'InternalResistance'`
        - **Alias**: `class_name`
    
    - `arbinLabel` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `arbinLabel`
    
    - `maccorLabel` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `maccorLabel`
    
    - `wikidataReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikidataReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `newareLabel` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `newareLabel`
    
    - `IEVReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `IEVReference`
    
    - `wikipediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikipediaReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = InternalResistance(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_9bf40017_3f58_4030_ada7_cb37a3dfda2d',
    
    class_name='InternalResistance',
    
    arbinLabel="example_value",
    
    maccorLabel="example_value",
    
    wikidataReference="example_value",
    
    elucidation="example_value",
    
    newareLabel="example_value",
    
    IEVReference="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_9bf40017_3f58_4030_ada7_cb37a3dfda2d',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'InternalResistance',
        alias="class_name"
    )
    
    arbinLabel: Optional[str] = Field(
        None,
        alias="arbinLabel"
    )
    
    maccorLabel: Optional[str] = Field(
        None,
        alias="maccorLabel"
    )
    
    wikidataReference: Optional[str] = Field(
        None,
        alias="wikidataReference"
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
    
    wikipediaReference: Optional[str] = Field(
        None,
        alias="wikipediaReference"
    )
    

    
    

    

    