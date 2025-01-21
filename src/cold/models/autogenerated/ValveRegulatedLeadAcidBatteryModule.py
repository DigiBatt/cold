
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .LeadAcidBatteryModule import LeadAcidBattery





from .ComponentModule import Component





class ValveRegulatedLeadAcidBattery(LeadAcidBattery):
    """
    Class representing the `ValveRegulatedLeadAcidBattery` entity, which inherits from:
    - LeadAcidBattery

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/battery#battery_0c7bde43_72dd_486c_a4a0_296bae9ccdc4'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ValveRegulatedLeadAcidBattery'`
        - **Alias**: `class_name`
    
    - `hasComponent` (`Optional[Component]`): 
        - **Default Value**: `None`
        - **Alias**: `hasComponent`
    
    - `wikidataReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikidataReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `IEVReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `IEVReference`
    
    - `wikipediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikipediaReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ValveRegulatedLeadAcidBattery(
    
    class_iri='https://w3id.org/emmo/domain/battery#battery_0c7bde43_72dd_486c_a4a0_296bae9ccdc4',
    
    class_name='ValveRegulatedLeadAcidBattery',
    
    hasComponent="example_value",
    
    wikidataReference="example_value",
    
    elucidation="example_value",
    
    IEVReference="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/battery#battery_0c7bde43_72dd_486c_a4a0_296bae9ccdc4',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ValveRegulatedLeadAcidBattery',
        alias="class_name"
    )
    
    hasComponent: Optional[Component] = Field(
        None,
        alias="hasComponent"
    )
    
    wikidataReference: Optional[str] = Field(
        None,
        alias="wikidataReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    IEVReference: Optional[str] = Field(
        None,
        alias="IEVReference"
    )
    
    wikipediaReference: Optional[str] = Field(
        None,
        alias="wikipediaReference"
    )
    

    
    @validator("hasComponent", pre=True, always=True)
    def validate_hasComponent(cls, value):
        if value is not None and not isinstance(value, Component):
            raise ValueError(f"Field 'hasComponent' must be an instance of 'Component' or its subclass.")
        return value
    
    

    

    