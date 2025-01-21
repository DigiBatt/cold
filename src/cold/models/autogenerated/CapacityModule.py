
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectricChargeModule import ElectricCharge



from .ElectrochemicalQuantityModule import ElectrochemicalQuantity



from .ISQDerivedQuantityModule import ISQDerivedQuantity







class Capacity(ElectricCharge, ElectrochemicalQuantity, ISQDerivedQuantity):
    """
    Class representing the `Capacity` entity, which inherits from:
    - ElectricCharge, ElectrochemicalQuantity, ISQDerivedQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_791c1915_a791_4450_acd8_7f94764743b5'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Capacity'`
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
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Capacity(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_791c1915_a791_4450_acd8_7f94764743b5',
    
    class_name='Capacity',
    
    maccorLabel="example_value",
    
    indigoLabel="example_value",
    
    novonixLabel="example_value",
    
    elucidation="example_value",
    
    newareLabel="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_791c1915_a791_4450_acd8_7f94764743b5',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Capacity',
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
    

    
    

    

    