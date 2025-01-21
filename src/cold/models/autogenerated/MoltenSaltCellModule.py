
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .NonAqueousCellModule import NonAqueousCell



from .BatteryCellModule import BatteryCell





from .ElectrolyteModule import Electrolyte





class MoltenSaltCell(NonAqueousCell, BatteryCell):
    """
    Class representing the `MoltenSaltCell` entity, which inherits from:
    - NonAqueousCell, BatteryCell

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/battery#battery_dae4c0f0_c3eb_4662_a0df_767e02014053'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MoltenSaltCell'`
        - **Alias**: `class_name`
    
    - `hasElectrolyte` (`Optional[Electrolyte]`): 
        - **Default Value**: `None`
        - **Alias**: `hasElectrolyte`
    
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
    obj = MoltenSaltCell(
    
    class_iri='https://w3id.org/emmo/domain/battery#battery_dae4c0f0_c3eb_4662_a0df_767e02014053',
    
    class_name='MoltenSaltCell',
    
    hasElectrolyte="example_value",
    
    wikidataReference="example_value",
    
    elucidation="example_value",
    
    IEVReference="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/battery#battery_dae4c0f0_c3eb_4662_a0df_767e02014053',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'MoltenSaltCell',
        alias="class_name"
    )
    
    hasElectrolyte: Optional[Electrolyte] = Field(
        None,
        alias="hasElectrolyte"
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
    

    
    @validator("hasElectrolyte", pre=True, always=True)
    def validate_hasElectrolyte(cls, value):
        if value is not None and not isinstance(value, Electrolyte):
            raise ValueError(f"Field 'hasElectrolyte' must be an instance of 'Electrolyte' or its subclass.")
        return value
    
    

    

    