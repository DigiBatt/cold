
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectricPotentialModule import ElectricPotential



from .ElectrochemicalQuantityModule import ElectrochemicalQuantity







class HalfWavePotential(ElectricPotential, ElectrochemicalQuantity):
    """
    Class representing the `HalfWavePotential` entity, which inherits from:
    - ElectricPotential, ElectrochemicalQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_2ae53fc6_d44d_41c9_acaf_c5606e6a981d'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'HalfWavePotential'`
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
    obj = HalfWavePotential(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_2ae53fc6_d44d_41c9_acaf_c5606e6a981d',
    
    class_name='HalfWavePotential',
    
    iupacReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_2ae53fc6_d44d_41c9_acaf_c5606e6a981d',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'HalfWavePotential',
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
    

    
    

    

    