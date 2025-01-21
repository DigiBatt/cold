
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectricPotentialModule import ElectricPotential



from .ElectrochemicalThermodynamicQuantityModule import ElectrochemicalThermodynamicQuantity







class ElectrochemicalStabilityLimit(ElectricPotential, ElectrochemicalThermodynamicQuantity):
    """
    Class representing the `ElectrochemicalStabilityLimit` entity, which inherits from:
    - ElectricPotential, ElectrochemicalThermodynamicQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_8f4b90ef_fea4_47c9_99f5_a9b3290a505d'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ElectrochemicalStabilityLimit'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ElectrochemicalStabilityLimit(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_8f4b90ef_fea4_47c9_99f5_a9b3290a505d',
    
    class_name='ElectrochemicalStabilityLimit',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_8f4b90ef_fea4_47c9_99f5_a9b3290a505d',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ElectrochemicalStabilityLimit',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    