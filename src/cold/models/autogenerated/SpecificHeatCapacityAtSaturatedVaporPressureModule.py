
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SpecificHeatCapacityModule import SpecificHeatCapacity







class SpecificHeatCapacityAtSaturatedVaporPressure(SpecificHeatCapacity):
    """
    Class representing the `SpecificHeatCapacityAtSaturatedVaporPressure` entity, which inherits from:
    - SpecificHeatCapacity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_b33909cc_61a1_4ab3_a1f8_d9283a6b1a0d'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SpecificHeatCapacityAtSaturatedVaporPressure'`
        - **Alias**: `class_name`
    
    - `qudtReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `qudtReference`
    
    - `wikidataReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikidataReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `ISO80000Reference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `ISO80000Reference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = SpecificHeatCapacityAtSaturatedVaporPressure(
    
    class_iri='https://w3id.org/emmo#EMMO_b33909cc_61a1_4ab3_a1f8_d9283a6b1a0d',
    
    class_name='SpecificHeatCapacityAtSaturatedVaporPressure',
    
    qudtReference="example_value",
    
    wikidataReference="example_value",
    
    elucidation="example_value",
    
    ISO80000Reference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_b33909cc_61a1_4ab3_a1f8_d9283a6b1a0d',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SpecificHeatCapacityAtSaturatedVaporPressure',
        alias="class_name"
    )
    
    qudtReference: Optional[str] = Field(
        None,
        alias="qudtReference"
    )
    
    wikidataReference: Optional[str] = Field(
        None,
        alias="wikidataReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    ISO80000Reference: Optional[str] = Field(
        None,
        alias="ISO80000Reference"
    )
    

    
    

    

    