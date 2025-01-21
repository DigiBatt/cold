
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ChargeDistributionModule import ChargeDistribution







class PulsedElectroacousticMethod(ChargeDistribution):
    """
    Class representing the `PulsedElectroacousticMethod` entity, which inherits from:
    - ChargeDistribution

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/characterisation-methodology/chameo#PulsedElectroacousticMethod'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'PulsedElectroacousticMethod'`
        - **Alias**: `class_name`
    
    - `iupacReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `iupacReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = PulsedElectroacousticMethod(
    
    class_iri='https://w3id.org/emmo/domain/characterisation-methodology/chameo#PulsedElectroacousticMethod',
    
    class_name='PulsedElectroacousticMethod',
    
    iupacReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/characterisation-methodology/chameo#PulsedElectroacousticMethod',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'PulsedElectroacousticMethod',
        alias="class_name"
    )
    
    iupacReference: Optional[str] = Field(
        None,
        alias="iupacReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    